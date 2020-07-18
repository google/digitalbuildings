package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Economizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_refrigerant_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_refrigerant_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_requirement;

/**
* Class Fan_ss_refm_ztm 
* Refrigerant level and zone temp monitoring fan.
*/
@SuppressWarnings("serial")
public class Fan_ss_refm_ztm extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IFan_ss_refm_ztm{

	IRI newInstance;
	public Fan_ss_refm_ztm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_refm_ztm"));
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


  public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode (){
		Set<IEconomizer_mode> UsesOptionalsEconomizer_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Economizer_mode) {
				UsesOptionalsEconomizer_mode.add((Economizer_mode)action);
			}
		});
		return UsesOptionalsEconomizer_mode;
	}


  public void addUsesZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_relative_humidity_sensor> getUsesZone_air_relative_humidity_sensor (){
		Set<IZone_air_relative_humidity_sensor> UsesZone_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_relative_humidity_sensor) {
				UsesZone_air_relative_humidity_sensor.add((Zone_air_relative_humidity_sensor)action);
			}
		});
		return UsesZone_air_relative_humidity_sensor;
	}


  public void addUsesZone_air_refrigerant_concentration_sensor (IZone_air_refrigerant_concentration_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_refrigerant_concentration_sensor> getUsesZone_air_refrigerant_concentration_sensor (){
		Set<IZone_air_refrigerant_concentration_sensor> UsesZone_air_refrigerant_concentration_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_refrigerant_concentration_sensor) {
				UsesZone_air_refrigerant_concentration_sensor.add((Zone_air_refrigerant_concentration_sensor)action);
			}
		});
		return UsesZone_air_refrigerant_concentration_sensor;
	}

	public static Set<IFan_ss_refm_ztm> getAllFan_ss_refm_ztmsObjectsCreated(){
		Set<IFan_ss_refm_ztm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_refm_ztm")).subjects().stream()
		.map(mapper->(IFan_ss_refm_ztm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}