package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IShade_extent_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Shade_extent_percentage_command;

/**
* Class Sdc_ext 
* Simple shade with extension control only.
*/
@SuppressWarnings("serial")
public class Sdc_ext extends www.google.com.digitalbuildings._0_0_1.hvac.Sdc implements ISdc_ext{

	IRI newInstance;
	public Sdc_ext(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesShade_extent_percentage_command (IShade_extent_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IShade_extent_percentage_command> getUsesShade_extent_percentage_command (){
		Set<IShade_extent_percentage_command> UsesShade_extent_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Shade_extent_percentage_command) {
				UsesShade_extent_percentage_command.add((Shade_extent_percentage_command)action);
			}
		});
		return UsesShade_extent_percentage_command;
	}

	public static Set<ISdc_ext> getAllSdc_extsObjectsCreated(){
		Set<ISdc_ext> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext")).subjects().stream()
		.map(mapper->(ISdc_ext)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}