package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_requirement;

/**
* Class Ahu 
* Tag for air-handling units.
*/
@SuppressWarnings("serial")
public class Ahu extends www.google.com.digitalbuildings._0_0_1.Equipment implements IAhu{

	IRI newInstance;
	public Ahu(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ahu"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsOutside_air_flowrate_requirement (IOutside_air_flowrate_requirement parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_flowrate_requirement> getUsesOptionalsOutside_air_flowrate_requirement (){
		Set<IOutside_air_flowrate_requirement> UsesOptionalsOutside_air_flowrate_requirement = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_requirement) {
				UsesOptionalsOutside_air_flowrate_requirement.add((Outside_air_flowrate_requirement)action);
			}
		});
		return UsesOptionalsOutside_air_flowrate_requirement;
	}

	public static Set<IAhu> getAllAhusObjectsCreated(){
		Set<IAhu> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ahu")).subjects().stream()
		.map(mapper->(IAhu)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}