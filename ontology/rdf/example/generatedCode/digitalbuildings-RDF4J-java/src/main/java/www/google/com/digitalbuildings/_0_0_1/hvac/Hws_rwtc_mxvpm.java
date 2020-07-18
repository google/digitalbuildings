package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IMixing_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Mixing_valve_percentage_command;

/**
* Class Hws_rwtc_mxvpm 
* Heating water system with mixed return temp control.
*/
@SuppressWarnings("serial")
public class Hws_rwtc_mxvpm extends www.google.com.digitalbuildings._0_0_1.hvac.Rwtc implements IHws_rwtc_mxvpm{

	IRI newInstance;
	public Hws_rwtc_mxvpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc_mxvpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesMixing_valve_percentage_command (IMixing_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixing_valve_percentage_command> getUsesMixing_valve_percentage_command (){
		Set<IMixing_valve_percentage_command> UsesMixing_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixing_valve_percentage_command) {
				UsesMixing_valve_percentage_command.add((Mixing_valve_percentage_command)action);
			}
		});
		return UsesMixing_valve_percentage_command;
	}

	public static Set<IHws_rwtc_mxvpm> getAllHws_rwtc_mxvpmsObjectsCreated(){
		Set<IHws_rwtc_mxvpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc_mxvpm")).subjects().stream()
		.map(mapper->(IHws_rwtc_mxvpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}