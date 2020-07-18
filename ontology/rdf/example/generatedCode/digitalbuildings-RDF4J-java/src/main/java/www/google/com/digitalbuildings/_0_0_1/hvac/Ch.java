package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.Equipment;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.Efficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Power_capacity;

/**
* Class Ch 
* Tag for chillers.
*/
@SuppressWarnings("serial")
public class Ch extends www.google.com.digitalbuildings._0_0_1.Equipment implements ICh{

	IRI newInstance;
	public Ch(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ch"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity (){
		Set<ICooling_thermal_power_capacity> UsesOptionalsCooling_thermal_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_thermal_power_capacity) {
				UsesOptionalsCooling_thermal_power_capacity.add((Cooling_thermal_power_capacity)action);
			}
		});
		return UsesOptionalsCooling_thermal_power_capacity;
	}


  public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification (){
		Set<IEfficiency_percentage_specification> UsesOptionalsEfficiency_percentage_specification = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Efficiency_percentage_specification) {
				UsesOptionalsEfficiency_percentage_specification.add((Efficiency_percentage_specification)action);
			}
		});
		return UsesOptionalsEfficiency_percentage_specification;
	}


  public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement (){
		Set<IFlowrate_requirement> UsesOptionalsFlowrate_requirement = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_requirement) {
				UsesOptionalsFlowrate_requirement.add((Flowrate_requirement)action);
			}
		});
		return UsesOptionalsFlowrate_requirement;
	}


  public void addUsesOptionalsPower_capacity (IPower_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IPower_capacity> getUsesOptionalsPower_capacity (){
		Set<IPower_capacity> UsesOptionalsPower_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Power_capacity) {
				UsesOptionalsPower_capacity.add((Power_capacity)action);
			}
		});
		return UsesOptionalsPower_capacity;
	}

	public static Set<ICh> getAllChsObjectsCreated(){
		Set<ICh> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ch")).subjects().stream()
		.map(mapper->(ICh)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}